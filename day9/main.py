import re, sys

def find_markers(input_text):
    markers = re.compile("\(\d+x\d+\)")
    marker_positions = []
    for marker in markers.finditer(input_text):
        start_point = marker.start()
        end_point = marker.start() + len(marker.group()) - 1 + int(marker.group().split('x')[0][1:])
        marker_positions.append([marker.group(), start_point, end_point])
    return marker_positions

def remove_overlaps(markers):
    for marker_index in range(0, len(markers)):
        text = markers[marker_index][0]
        start = markers[marker_index][1]
        end = markers[marker_index][2]
        inner_index = marker_index+1
        
        # Basically, remove markers whose start point is before the current one's end point
        while inner_index <= len(markers) - 1 and markers[inner_index][1] < end:
            markers.remove(markers[inner_index])
        # Do a range check, removing markers may mean we are already done
        if marker_index + 1 >= len(markers):
            break
    return markers

def build_final_string(input_text, markers):
    final_string = ''
    # Add the characters from the start to the first marker
    final_string += input_text[0:markers[0][1]]

    for marker_index in range(0, len(markers)):
        marker = markers[marker_index]
        start = marker[1] + len(marker[0])
        end = marker[2] + 1
        # The amount of times the text has to be repeated
        # The split will get 7) from (140x7) so I use [:-1]
        multiplier = int(marker[0].split('x')[1][:-1])
        # First add the remaining text from the end of the previous marker to the start of the current one
        final_string += input_text[markers[marker_index-1][2]+1:marker[1]]
        # Now add the text from the current marker (multiplier x text)
        final_string += multiplier * input_text[start:end]
    # Add the text from the end of the last marker to the end of the input file
    final_string += input_text[markers[len(markers)-1][2]+1:]
    return final_string

def main():
    input_text = open('input.txt', 'r') .read()
    # re.match(r'\(\d+x\d+\)', '(143x8)').group()
    markers_with_endpoints = remove_overlaps(find_markers(input_text))
    
    print(len(build_final_string(input_text, markers_with_endpoints)))

if __name__ == '__main__':
    main()