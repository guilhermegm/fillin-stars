import re
import requests
import env

def get_file_content(file_path):
    f = open(file_path, 'r')
    file_content = f.read()
    f.close()
    return file_content

def get_repo_details(repo_github_name):
    github_api_url = 'https://api.github.com/repos/{}'.format(repo_github_name)
    call = requests.get(github_api_url, headers = {
        'Authorization': 'token {}'.format(env.GITHUB_TOKEN)
    })
    return call.json() if requests.codes.ok else None

def fillin_repo_stars(file_content_line):
    find_github_url = re.findall(r'\(https*://github.com/(.*?/.*?)\)', file_content_line, re.I)
    repo_github_name = find_github_url[0] if find_github_url else None
    is_repo_line_startswith = file_content_line.startswith(env.REPO_LINE_STARTSWITH) \
        if env.REPO_LINE_STARTSWITH else True

    if is_repo_line_startswith and repo_github_name:
        repo_details = get_repo_details(repo_github_name)

        if not repo_details:
            raise Exception('Could not get repository details')

        if env.REMOVE_REPO_STAR:
            file_content_line = env.REMOVE_REPO_STAR(file_content_line)

        return env.FILL_REPO_STAR(file_content_line, repo_details)

    return file_content_line

def parse_file_content_list(file_content_list):
    if env.FILL_FOOTER_INFO:
        file_content_list.append('')
        file_content_list.append(env.FILL_FOOTER_INFO)

    new_file_content = '\n'.join(file_content_list)
    return new_file_content

def save_file(file_content):
    f = open(env.FILE_OUTPUT_PATH, 'w+')
    f.write(file_content)
    f.close()

file_content = get_file_content(env.FILE_PATH)
file_content_list = file_content.split('\n')
file_content_list = list(map(fillin_repo_stars, file_content_list))
new_file_content = parse_file_content_list(file_content_list)
save_file(new_file_content)
