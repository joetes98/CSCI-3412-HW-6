from heapq import heappush, heappop, heapify
from collections import Counter
from bitarray import bitarray, decodetree
import math
import os

def huffmanCode(aDict): #with a given dictionary

    heap = [[freq, [aChar, ""]] for aChar, freq in aDict.items()] # build a minheap
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap) # pop least frequent, then heapify
        hi = heappop(heap) # next least frequent , then heapify
        for pair in lo[1:]:
            pair[1] = '0' + pair[1] #pair[1] is the current codeword for pair[0] char
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:]) #push then heapify
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def zip(text, fileName, huffman):
    with open(text, 'r') as file:
        textString = file.read()
        
    ba = bitarray()
    for i in textString:
        ba.extend(huffman[i]) # encode text using huffman code
        
    with open(fileName, 'wb') as zipFile:
        ba.tofile(zipFile) # write the bitarray to file

    return len(ba)


def unzip(zipFileName, huffman, zipSize):
    bitStrStream = ""
    text = ""
    # read zip file and convert to bit string
    with open(zipFileName, 'rb') as zipFile:
        for byte in zipFile.read():
            bitStrStream += format(byte, '08b')
    
        
    # resize bitStrStream
    bitStrStream = bitStrStream[:zipSize]

    # decoding step
    while len(bitStrStream) > 0:
        matched = False # huffman code match tracker for debugging
        for k, v in huffman.items():
            if bitStrStream.startswith(v):
                text += k
                bitStrStream = bitStrStream[len(v):]
                matched = True
                break
        if not matched:
            print("Error: No match found")
            break
     
    outputName = os.path.splitext(zipFileName)[0] + ".unzipped.txt"
    with open(outputName, 'w') as textFile:
        textFile.write(text)

    return outputName
     

def main():

    print("Enter a file to zip: ")
    inputFile = input()

    with open(inputFile, 'r') as file:
        text = file.read()

    count = Counter(text)
    huffmanList = huffmanCode(count)
    huffman = {char: bitarray(code) for char, code in huffmanList}
    
    # Print table header
    print(f"{'character':<12}{'Weight':>10}{'Huffman Code':>20}")
    for char, code in sorted(huffmanList, key=lambda x: count[x[0]], reverse=True):
        if char == ' ':
            display = "' '"
        elif char == '\n':
            display = "'\\n'"
        else:
            display = char
        print(f"{display:<12}{count[char]:>10}{code:>20}")

    # Cost calculation
    huffmanCost = sum(count[char] * len(code) for char, code in huffmanList)
    asciiCost = sum(count[char] * 8 for char in count)
    fclLength = math.ceil(math.log2(len(count)))
    fclCost = sum(count[char] * fclLength for char in count)

    # Huffman efficiencies
    asciiEfficiency = round((asciiCost - huffmanCost) / huffmanCost * 100)
    fclEfficiency = round((fclCost - huffmanCost) / huffmanCost * 100)

    # ZIP
    bitLength = zip(inputFile, "huffman.zip", huffman)
    print(f"\n{inputFile} zipped to huffman.zip")

    # UNZIP
    huffmanDecode = {char: code.to01() for char, code in huffman.items()}
    unzippedName = unzip("huffman.zip", huffmanDecode, bitLength)

    # File sizes
    inputSize = os.path.getsize(inputFile)
    zipSize = os.path.getsize("huffman.zip")
    unzippedSize = os.path.getsize(unzippedName)

    # Print cost and file size
    print(f"\nExpected cost of Huffman code: {huffmanCost}")
    print(f"Expected cost of ASCII code: {asciiCost}")
    print(f"Huffman efficiency improvement over ASCII code: {asciiEfficiency}%")
    print(f"Expected cost of optimal FCL code: {fclCost}")
    print(f"Huffman efficiency improvement over FCL: {fclEfficiency}%")

    print(f"The size of {inputFile}: {inputSize}")
    print(f"The size of huffman.zip: {zipSize}")
    print(f"The size of {unzippedName}: {unzippedSize}")

if __name__ == "__main__":
    main()