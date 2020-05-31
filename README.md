# Player

## How it works
 - We will receive a submission from the user.
 - We will store it inside this project (dirname=submission)
 - Depending on the format, we will either import it or use stdin/stdout for communication
 - Users don't know about this repo, all they submit will be copied to submissions and done

## Suported formats
 - python package
 - executables

## Things to keep in mind
 - regardless of format, keep `__init__.py` and `requirements.txt` inside submission

## Testing
For the format you want to test,
```sh
mv sample-$FORMAT submission
python3 main.py
```
