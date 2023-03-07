import pandas as pd

print('Reading JSON review file...')
df = pd.read_json(r'../data/Video_games_5.json', lines=True)
print('Successfully read Video Games Review JSON file.')

print('Converting "reviewText" column type to string...')
df['reviewText'] = df['reviewText'].astype(pd.StringDtype())
print('Conversion complete.')

# Clean Review data text
df['reviewText'] = df['reviewText'].str.replace('\n', ' ')

outfile = r'../data/vg_review_text_only.csv'
print('Writing text-only reviews to', outfile, '...')
df.loc[:,'reviewText'].str.strip(r'"').to_csv(outfile, header=False, index=False)
print('Output complete.')

