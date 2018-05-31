def calcBuffer(screen, buffer2, buffer1, dampening, startRow, endRow, startCol, endCol):
    for i in range(startRow, endRow):
        for j in range(startCol, endCol):
            if i > 0 and i < endRow-1 and j > 0 and j < endCol-1:
                buffer2[i][j] = ((buffer1[i-1][j]+
                                 buffer1[i+1][j]+
                                 buffer1[i][j-1]+
                                 buffer1[i][j+1])/2 - buffer2[i][j]) * dampening

            color = buffer2[i][j]
            if color > 255:
                color = 255
            elif color < 0:
                color = 0
            screen.set_at((i,j), (color,color,color))
