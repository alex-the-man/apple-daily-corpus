DATA_PATH=data
OUTPUT_PATH=corpus

all: data corpus

data:
	@if [ ! -d "data" ]; then \
    		echo "Cannot find directory data. Please unzip apple-articles-plaintext-20020101-20210620.zip to the project directory."; \
   		exit 1; \
	fi

corpus:
	mkdir corpus
	find $(DATA_PATH) -maxdepth 1 ! -path $(DATA_PATH) -type d | xargs -l -P `nproc` -I daily_folder ./apple2csv.py daily_folder $(OUTPUT_PATH) ;

clean:
	rm -rf corpus
