import csv

# Define input and output file paths
input_file = 'day30_flashcards_en_fr/fr_50k.txt'
output_file = 'day30_flashcards_en_fr/fr_100words.csv'

# Open the input file for reading and output file for writing
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_writer = csv.writer(outfile)
    
    # Write header row
    csv_writer.writerow(['word', 'number'])
    count = 0
    # Process each line in the input file
    for line in infile:
        # Split the line into word and number
        parts = line.split()
        if len(parts) >= 2:
            word = parts[0]
            number = parts[1]
            # Write to the CSV file
            csv_writer.writerow([word, number])
            count +=1

            if count >=100:
                break
print("Transformation complete. The CSV file has been created.")
