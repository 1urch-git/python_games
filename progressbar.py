"""Progress Bar Simulation"""

import random, time

BAR = chr(9608) #This character is a black box

def main():
    #Simulate a download; this can be resused in functional code
    print('Progress Bar Simulation')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        #"Download" a random amount of bytes
        bytesDownloaded += random.randint(0,100)

        #Get the progress bar string for this amount of progress
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        #Don't print a newline at the end, and immediately flush the printed string to the screen
        print(barStr, end='', flush=True)
        time.sleep(0.2) #pause for a moment

        #print backspaces to move the text cursor to the lines' start
        print('\b' * len(barStr), end='', flush=True)

def getProgressBar(progress, total, barWidth=40):
    """Return a string that represents a progress bar that has barWidth bars and has progressed progress amounts of a total time"""
    progressBar = '' #the progress bar will be a string value
    progressBar += '[' #Create the left end of the progress bar

    #Make sure that the amount of progress is between 0 and total
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0
    
    #Calculate the number of "bars" to display
    numberOfBars = int((progress/total) * barWidth)

    progressBar += BAR * numberOfBars #add to the progress bar
    progressBar += ' ' * (barWidth - numberOfBars) #add empty space
    progressBar += ']' #Add the right end of the progress bar

    #calculate the percentage complete
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%' #add a percentage
    #add the numbers
    progressBar += ' ' + str(progress) + '/' + str(total)

    return progressBar #return progess abr string

if __name__ == '__main__':
    main()
