#!/usr/bin/env python3

"""
Matchering CLI
~~~~~~~~~~~~~~~~~~~~~

Simple Matchering 2.0 Command Line Application.

:copyright: (C) 2016-2022 Sergree
:license: GPLv3, see LICENSE for more details.

"""

import matchering as mg
from argparse import ArgumentParser
import logging
import sys, os
from pathlib import Path


# 현재 .py파일이 존재하는 경로
app_path = os.path.dirname(os.path.realpath(__file__))
# os.chdir(app_path)

# 레퍼런스용 프리셋 생성(references폴더에서 하위 폴더 만들고 음악 파일 넣기(.mp3, .wav, .aac, .flac)) 
# 폴더명은 소문자만 사용. 음악파일은 폴더당 하나만 넣어야함.
def reference_preset():
    reference_path = Path(f"{app_path}/references")
    # 레퍼런스 폴더의 구조를 읽어들여서 preset_list 딕셔너리 생성
    preset_list = {}    
    for folder in reference_path.iterdir():
        if folder.is_dir():            
            files = [str(entry) for entry in folder.iterdir() if entry.is_file() and entry.suffix.lower() in ['.mp3', '.wav', '.aac', '.flac']]                        
            if files:
                preset_list[folder.name] = files[0]        
    return preset_list


# 레퍼런스 정의(파일인지 프리셋인지)
def is_file_or_preset(value):
    # 입력값과 딕셔너리의 대소문자를 통일시켜 비교
    value_lower = value.lower()

    # 파일 경로가 존재하는지 확인
    if Path(value).is_file():
        return value
    # 프리셋 딕셔너리에서 가져올 수 있는지 확인
    elif value_lower in (preset.lower() for preset in reference_preset()):
        return reference_preset()[value_lower]
    else:
        raise ValueError(f"입력값 '{value}'은(는) 유효한 파일 경로 또는 프리셋이 아닙니다.")


def parse_args():    
    parser = ArgumentParser(
        description="Matchering 2.0 CLI(Command Line Application) modified by BoniK"
    )
    parser.add_argument("target", type=str, help="마스터링 대상 오디오")
    parser.add_argument(
        "reference",
        type=is_file_or_preset,        
        help=f'레퍼런스 오디오. 프리셋 선택가능 {list(reference_preset().keys())}'
    )
    parser.add_argument("result", type=str, help="결과물을 저장할 경로")
    parser.add_argument(
        "-b",
        "--bit",
        type=int,
        choices=[16, 24, 32],
        default=16,
        help="마스터링 결과의 bit depth. 기본값 16. 32는 32-bit float",
    )
    parser.add_argument(
        "--log",
        type=str,
        default=None,
        help="로그가 기록될 파일",
    )
    parser.add_argument(
        "--no_limiter",
        dest="no_limiter",
        action="store_true",
        help="마지막 단계에서 리미터를 비활성합니다.",
    )
    parser.add_argument(
        "--dont_normalize",
        dest="dont_normalize",
        action="store_true",
        help="--no_limiter 설정시 노멀라이징을 비활성합니다."
        "bit depth가 32가 아니라면 클리핑을 발생시킬 수 있습니다.",
    )
    return parser.parse_args()


def set_logger(handler, formatter, logger):
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def prepare_logger(args):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("{asctime}: {levelname:>7}: {message}", style="{")

    if args.log:
        set_logger(logging.FileHandler(args.log), formatter, logger)

    set_logger(logging.StreamHandler(sys.stdout), formatter, logger)

    return args, logger


def run(args, logger):
    mg.log(
        warning_handler=logger.warning,
        info_handler=logger.info,
        debug_handler=logger.debug,
    )

    bit_to_subtype = {16: "PCM_16", 24: "PCM_24", 32: "FLOAT"}

    logger.debug(f"{mg.__title__} {mg.__version__}")
    logger.debug(f"Maintained by {mg.__author__}: {mg.__email__}")
    logger.debug(f'Contributors: {", ".join(mg.__credits__)}')

    try:
        mg.process(
            target=args.target,
            reference=args.reference,
            results=[
                mg.Result(
                    args.result,
                    bit_to_subtype.get(args.bit),
                    use_limiter=not args.no_limiter,
                    normalize=not args.dont_normalize,
                )
            ],
        )
    except Exception as e:
        logger.exception("Got the exception while executing mg.process()")


if __name__ == "__main__":
    run(*prepare_logger(parse_args()))
