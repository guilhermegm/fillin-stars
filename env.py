import os
import re
import datetime

def remove_repo_star(repo_line, star_prefix = ':star: '):
    new_repo_line = re.sub(
      r'(.*?\[.*?\]\(.*?\)) (\(.*?\))(.*?)',
      r'\1\3'.format(star_prefix, repo_details['stargazers_count']),
      repo_line,
      count = 1
    )
    print(new_repo_line)
    return new_repo_line

def fill_repo_star(repo_line, repo_details, star_prefix = ':star: '):
  try:
    new_repo_line = re.sub(
      r'(.*?\[.*?\]\(.*?\))(.*?)',
      r'\1 ({}{})\2'.format(star_prefix, repo_details['stargazers_count']),
      repo_line,
      count = 1
    )
    print(new_repo_line)
    return new_repo_line
  except:
    return repo_line

FILE_PATH = './README.md'
FILE_OUTPUT_PATH = './stars-README.md'
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN') # https://developer.github.com/v3/auth/#basic-authentication
REPO_LINE_STARTSWITH = ('* [', '    * [')
FILL_REPO_STAR = fill_repo_star
REMOVE_REPO_STAR = remove_repo_star
FILL_FOOTER_INFO = '*The repository\'s stars were updated last at {} (UTC)*'.format(datetime.datetime.utcnow().strftime('%m/%d/%Y - %H:%M'))
