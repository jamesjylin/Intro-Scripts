import os

# Change revision, date, and directory, and run the program, leave everything else
# Function to rename multiple files
def main():

    # Copy the location of the files in the quotations. Make sure to include double backspaces.
    # E.g. "C:\\Users\\pass.ecs.coop\\Desktop"
    directory = "C:\\Users\\pass.ecs.coop\\Desktop\\Test Files"

    # Revision number: if revision is PG2, set revision = "2"
    revision = "2"

    # Date: set to desired date format within quotations
    date = "MAR 11, 2020"

    os.chdir(directory)

    # Loop through directory
    for filename in os.listdir():

        # Finds length of file name, removes ending (PG# DATE) to be replaced
        i = 0
        for i in range(len(filename)-1, 0, -1):
            if filename[i] == "(":
                break

        # Renames files
        src = filename
        dst = filename[:i] + "(PG" + revision + " " + date + ").pdf"
        os.rename(src, dst)


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()