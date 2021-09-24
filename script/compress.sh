files=""
cd PIT_sudoku_DAMASE_Lucas
for f in *; do
	if [ ! $f = "sudoku_db.txt" ]; then
		files=$files" "$f
	fi
done
tar -cf ../PIT_sudoku_DAMASE_Lucas.tar.gz $files