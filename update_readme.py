import random
import argparse

def read_file(filename):

    with open(filename, 'r') as f:
        data = f.read()
    return data

def get_introduction(data, categories):
    return data.split(f"## {categories[0]}\n")[0]

def get_body_parts(data, categories):
    extended_categories = categories+['TOKENTHATDOESNOTEXIST']
    # for idx in range(len(extended_categories)-1):
    #     try:
    #         data.split(f"## {extended_categories[idx]}")[1].split(f"## {extended_categories[idx+1]}")[0]
    #     except:
    #         print(idx)
    body_parts = [
        data.split(f"## {extended_categories[idx]}\n")[1].split(f"\n## {extended_categories[idx+1]}")[0]
        for idx in range(len(extended_categories)-1)]
    return body_parts

def reconstruct_data(categories, introduction, body_parts):
    assert len(categories) == len(body_parts)
    body = '\n'.join([f'## {title}' + '\n' + articles for title, articles in zip(categories, body_parts)])
    text = introduction + body
    return text

def save_data(filename, data):
    with open(filename, "w") as f:
        f.write(data)

def get_scores(text_body, categories):
    scores = dict()
    for idx, category in enumerate(categories):
        body_part = text_body[idx]
        unread_count = body_part.count('❌')
        read_count = body_part.count('✅')
        total = read_count+unread_count
        # print(body_part)
        scores[category] = f'{100*read_count/total:.0f}% ({read_count}/{total})'
    return scores

def get_unread_papers(text_body, categories):
    unread_papers = dict()
    for idx, category in enumerate(categories):
        body_part = text_body[idx]
        extracted_papers = [x.split('❌ ')[1] for x in body_part.split('\\\n') if len(x)>0 and '❌' in x]
        unread_papers[category] = extracted_papers
    return unread_papers

def update_introduction(text_introduction, categories, scores, unread_papers):
    progress_text = ""
    for idx, category in enumerate(categories):
        progress_text += f"{category}: {scores[category]}"
        recommended_paper = '**Congrats you read them all**'
        if len(unread_papers[category])>0:
            recommended_paper = random.choice(unread_papers[category])
        progress_text += f", recommendation: {recommended_paper}"
        if idx<len(categories):
            progress_text += "\\\n"

    random_paper = '**Congrats you read them all**'
    categories_to_choose_from = [category for category in categories if len(unread_papers[category])>0]
    if len(categories_to_choose_from)>0:
        random_paper = random.choice(unread_papers[random.choice(categories_to_choose_from)])


    rec_splitter = "**Recommended Paper**"
    init_content = text_introduction.split(rec_splitter,maxsplit=1)[0]

    prog_splitter = "**Progress**"

    toc_splitter = "**Table of Contents**"
    table_of_contents = toc_splitter+text_introduction.split(toc_splitter, maxsplit=1)[1]

    new_introduction = f"""{init_content}{rec_splitter}
{random_paper}

{prog_splitter}
{progress_text}
{table_of_contents}"""
    return new_introduction

def get_categories(data):
    categories = [
        x.split('](#')[0].split('. [')[1] 
        for x in data.split("## Data Quality")[0].split('\n')
            if (len(x)>0 and len(x.split('. ')) 
            and x.split('. ')[0].isdigit()>0
            )
    ]
    return categories

def update_readme(filename):
    data = read_file(filename)
    categories = get_categories(data)

    text_body = get_body_parts(data, categories)
    text_introduction = get_introduction(data, categories)

    unread_papers = get_unread_papers(text_body, categories)
    scores = get_scores(text_body, categories)

    new_introduction = update_introduction(text_introduction, categories, scores, unread_papers)
    reconstructed_text = reconstruct_data(categories, new_introduction, text_body)
    
    save_data(filename, reconstructed_text)


if __name__=='__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--filepath')

    args = parser.parse_args()
    update_readme(args.filepath)
