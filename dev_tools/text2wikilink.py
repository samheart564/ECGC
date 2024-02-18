def generate_wiki_link(page_name):
    # Construct the URL based on the page name
    base_url = "https://azurlane.koumakan.jp/wiki/"
    formatted_page_name = page_name.replace(" ", "_")
    full_url = base_url + formatted_page_name

    # Generate the HTML link
    link_html = f'<a rel="noopener noreferrer" target="_blank" href="{full_url}" title="{page_name}">{page_name}</a>'

    return link_html

def append_to_html_file(file_name, link):
    # Append the link to the existing HTML file
    with open(file_name, "a") as file:
        file.write(link)

def main():
    # Get user input for the page name
    page_name = input("Enter the page name: ")

    # Generate the link
    link = generate_wiki_link(page_name)

    # Append the link to test1.html
    append_to_html_file("test1.html", link)

    print(f"Link appended to test1.html: {link}")

if __name__ == "__main__":
    main()
