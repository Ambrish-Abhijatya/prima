def input_text():
    return input('- Text: ')

def plain():
    return input_text()
    
def bold():
    return '**' + input_text() + '**'

def italic():
    return '*' + input_text() + '*'

def link():
    label = input('- Label')
    url = input('- url')
    return f'[{label}]({url})'

def inline_code():
    return '`' + input_text() + '`'
    
def header():
    level = int(input('- Level'))
    if 1 <= level <= 6 :
        return '#' * level + ' ' + input_text()
    else:
        print('The level should be between 1 and 6.')

def line_break():
    return '\n'
def main():
    formatters = ['plain', 'bold', 'italic', 'link', 'inline-code', 'header', 'line-break']
    while True:
        prompt = input('Choose a formatter: ')
        returnText = ''
        lines = []
        if prompt not in formatters:
            if prompt == '!help':
                print('Available formatters: plain bold italic link inline-code header line-break')
                print('Special commands: !help !done')
            elif prompt == '!done':
                break
            else:
                print('Unknown formatting type or command. Please try again')
        else:
            if prompt == 'plain':
                returnText = plain()
            elif prompt == 'bold':
                returnText = bold()
            elif prompt == 'italic':
                returnText = italic()
            elif prompt == 'link':
                returnText = link()
            elif prompt == 'inline-code':
                returnText = inline_code()
            elif prompt == 'header':
                returnText = header()
            elif prompt == 'line-break':
                returnText = line_break()
        if returnText:
            lines.append(returnText)
        print(*lines, sep="")

if __name__ == '__main__':
    main()

            
    