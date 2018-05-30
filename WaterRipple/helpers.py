def calcBuffer(buffer2, buffer1, dampening, startRow, endRow, startCol, endCol):
    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            buffer2[i][j] = ((buffer1[i-1][j]+
                             buffer1[i+1][j]+
                             buffer1[i][j-1]+
                             buffer1[i][j+1])/2 - buffer2[i][j]) * dampening

def setScreen(screen, buffer2, startRow, endRow, startCol, endCol):
    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            color = (buffer2[i][j])
            if color > 255:
                color = 255
            elif color < 0:
                color = 0
            screen.set_at((i,j), (color,color,color))
