[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://pip.me/sergree)

# Matchering CLI

### Simple Matchering 2.0 Command Line Application (customized by BoniK)

Compact and easy-to-use CLI app for working with the **[Matchering python library][matchering]**. Use it for audio batch processing.

## Features

- File logging
- 16-bit, 24-bit, and 32-bit float results
- Setting to disable the built-in *Matchering limiter* and *normalization*

## Installation

### Ubuntu 20.04 LTS

1. Install the necessary dependencies

```sudo apt update && sudo apt -y install libsndfile1 ffmpeg python3-pip```

2. Clone the repo and move to the directory

```git clone https://github.com/sergree/matchering-cli && cd matchering-cli```

3. Install dependencies from `requirements.txt`

```python3 -m pip install -r requirements.txt```

### Windows 10

1. Install **[Anaconda Python/R Distribution][anaconda]**

2. Install **[FFmpeg]** to `C:\ffmpeg` and add `C:\ffmpeg\bin` to the PATH variable

**[HOWTO][path]**

3. Run **Anaconda Prompt (Anaconda3)** and move to the cloned `matchering-cli` directory

```cd C:\Users\<your_username>\Downloads\matchering-cli```

4. Install dependencies from `requirements.txt`

```python -m pip install -r requirements.txt```

## Usage

- Get the WAV 16-bit result

```python3 mg_cli.py my_song.wav some_popular_song.wav my_song_master_16bit.wav```

- Get the WAV 16-bit result and save the log file `process.log`

```python3 mg_cli.py my_song.wav some_popular_song.wav my_song_master_16bit.wav --log process.log```

- Get the normalized WAV 24-bit result without applying a limiter

```python3 mg_cli.py target.wav reference.wav result_24bit.wav -b24 --no_limiter```

- Get the non-normalized WAV 32-bit result without applying a limiter

```python3 mg_cli.py target.wav reference.wav result_32bit.wav -b32 --no_limiter --dont_normalize```


##### *Use `python` in Windows instead of `python3`*

Also you can run it without `python3` in front, if `mg_cli.py` has `+x` permission:

```sudo chmod +x mg_cli.py```

And then:

```./mg_cli.py my_song.wav some_popular_song.wav my_song_master_16bit.wav```

```
usage: mg_cli.py [-h] [-b {16,24,32}] [--log LOG] [--no_limiter] [--dont_normalize] [--aac] [--del_target] target reference result

Matchering 2.0 CLI(Command Line Application) modified by BoniK

positional arguments:
  target                마스터링 대상 오디오
  reference             레퍼런스 오디오. 프리셋 선택가능 ['ballad', 'dance', 'default', 'folk', 'pop']
  result                결과물을 저장할 경로

options:
  -h, --help            show this help message and exit
  -b {16,24,32}, --bit {16,24,32}
                        마스터링 결과의 bit depth. 기본값 16. 32는 32-bit float
  --log LOG             로그가 기록될 파일
  --no_limiter          마지막 단계에서 리미터를 비활성합니다.
  --dont_normalize      --no_limiter 설정시 노멀라이징을 비활성합니다.bit depth가 32가 아니라면 클리핑을 발생시킬 수 있습니다.
  --aac                 --aac 마스터링된 wav를 다시 aac로 변환합니다.
  --del_target          --del_target 원본(target) 파일을 삭제합니다.                
```

### 프리셋 만들기
reference 폴더 안에 원하는 프리셋명으로 폴더 작성
각 폴더 마다 하나의 wav파일을 넣으면 됩니다.


### Visit **[Matchering main repo][matchering]** to learn more about it!

### 수정판 작성자 보닉의 블로그 **[그늘진 낙원][bonik's blog]** to learn more about it!

## A Coffee(원작자의 링크)

If our script saved your time or money, you may:

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://pip.me/sergree)

**Thank you!**

[bonik's blog]: https://bonik.me
[matchering]: https://github.com/sergree/matchering
[anaconda]: https://www.anaconda.com/products/individual#Downloads
[FFmpeg]: https://www.ffmpeg.org/download.html
[path]: https://video.stackexchange.com/questions/20495/how-do-i-set-up-and-use-ffmpeg-in-windows
