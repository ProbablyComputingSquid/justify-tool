#################################
# justify ez                    #
# a program by @ComputingSquid  #
# version 1.0                   #
# Made on replit                #
# All original code             #
#################################

from math import floor


def justify(words, width):
    """
    :param words: a list of strings
    :param width: an integer
    :return: an array containing text
    """
    print("Justifying string with width of", width)
    print("-" * width)
    words = words.split(' ')
    justified = []
    line = []
    for word in words:
        # if the word can fit in the width
        if len(word) + len(' '.join(line)) < width:
            line.append(word)
        elif len(word) > width:
            # word length greater than the width
            # split the word into multiple lines
            # and add each line to the justified array
            for i in range(floor(len(word) / width)):
                justified.append(word[i * width:(i+1) * width - 1] + "-")
            #pass
        else:
            # do some things with the spaces
            spacer = ' '
            if len(line) == 1 or len(spacer.join(line)) == width:
                pass
            else:
                # extra space should be a int rn
                # find the amount of empty space
                extra_space = width - len(''.join(line))
                # divide it by the actual length of the line minus one because idk
                extra_space /= len(line) - 1
                # round it
                extra_space = floor(extra_space)
                # multiple the spacer by the amount of extra space
                spacer *= extra_space
                #print(extra_space)
            line = spacer.join(line)
            justified.append(line)
            line = []
            line.append(word)
    return justified
    
to_justify = input("enter string to justify>>>")
# text_width could be anything, but i've made it this lol
# text_width = "69420"
text_width = int(input("enter width in characters (whitespaces count!)>>>"))
while (type(text_width) is not int):
    try:
        text_width = int(input("enter width in characters (whitespaces count!)>>>"))
        if text_width < 10:
            print("text width is recommended to be above 10, unexpected behavior may occur")
    except ValueError:
        print("enter a number bruh")

#debug purposes only
to_justify = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus euismod blandit tempus. Maecenas non dolor sit amet nisi sollicitudin sodales. Aliquam bibendum ligula id tellus molestie, sit amet ornare nibh lacinia. Quisque pretium vestibulum leo, vel fermentum dolor condimentum vel. Pellentesque porta, neque at interdum convallis, augue orci viverra metus, eget placerat enim lorem ac lorem. Fusce interdum elit nec felis venenatis tempus id ac risus. Nulla luctus scelerisque tincidunt. Sed quis felis malesuada, faucibus mauris vitae, ornare diam. Phasellus venenatis, ex ac vehicula dapibus, nunc diam facilisis tellus, quis lobortis augue metus in nulla. Vivamus at sagittis metus. Etiam scelerisque neque ante, at pretium felis rutrum nec. Duis at velit sit amet justo blandit porttitor sit amet nec erat. Duis tincidunt nunc quam, vitae aliquet turpis elementum ac. Quisque dignissim quam sed ante rutrum malesuada. Cras ultrices, tellus in feugiat bibendum, odio orci viverra enim, nec scelerisque justo mauris quis justo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus volutpat ligula elementum ligula volutpat eleifend. Ut mi nisi, convallis sit amet justo non, malesuada fringilla ipsum. Etiam ut cursus nisl, eget egestas dui. Morbi eget gravida metus. Phasellus commodo vestibulum metus, id consectetur eros semper et. Pellentesque varius diam eget enim vestibulum auctor. Curabitur varius risus augue, in ultricies lorem sagittis ac. Donec et lacus metus. Donec sed congue augue. Proin in metus sit amet diam pharetra varius. In pulvinar consectetur augue, ut pharetra tellus dignissim ut. Fusce fermentum risus vel sapien pretium, sed pharetra nisl sodales. Nullam efficitur ac quam sed dapibus. Cras vel molestie dolor. Sed suscipit rhoncus leo, vitae molestie erat eleifend in. Ut et tempus sem. Vivamus placerat libero non nisl maximus, a luctus turpis gravida"

# prints out the justified text
for i in justify(to_justify, text_width):
    print("\'" + i + "\'")
