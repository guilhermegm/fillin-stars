import os
import re
import datetime

stars_emoji = ':star:'
watchers_emoji = ':eyeglasses:'

def remove_repo_star(repo_line):
    new_repo_line = re.sub(
        r'(.*?\[.*?\]\(.*?\)) (\(.*?\))(.*?)',
        r'\1\3',
        repo_line,
        count = 1
    )
    return new_repo_line

def fill_repo_star(repo_line, repo_details):
  try:
    stargazers_count = repo_details['stargazers_count']
    subscribers_count = repo_details['subscribers_count']

    new_repo_line = re.sub(
        r'(.*?\[.*?\]\(.*?\))(.*?)',
        r'\1 ({}{} {}{})\2'.format(
          stars_emoji,
          stargazers_count,
          watchers_emoji,
          subscribers_count
        ),
        repo_line,
        count = 1
    )
    print(new_repo_line)
    return new_repo_line
  except Exception as e:
    raise e
    return repo_line

FILE_PATH = './README-test.md'
FILE_OUTPUT_PATH = './stars-README-test.md'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN') # https://developer.github.com/v3/auth/#basic-authentication
REPO_LINE_STARTSWITH = ('* [', '    * [') # opcional
FILL_REPO_STAR = fill_repo_star
REMOVE_REPO_STAR = None # opcional
FILL_FOOTER_INFO = '*The repository\'s stars were updated last at {} (UTC)*'.format(datetime.datetime.utcnow().strftime('%m/%d/%Y - %H:%M'))
