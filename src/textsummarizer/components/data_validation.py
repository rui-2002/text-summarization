import os
from textsummarizer.logging import logger
from textsummarizer.entity import DataValidationConfig



class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config = config
    
    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = True
            
            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            
            # Debug print
            print("Required files:", self.config.ALL_REQUIRED_FILES)
            print("Files present in directory:", all_files)
            
            missing_files = []
            for required_file in self.config.ALL_REQUIRED_FILES:
                if required_file not in all_files:
                    missing_files.append(required_file)
                    validation_status = False
            
            # Debug print
            if missing_files:
                print("Missing files:", missing_files)
                
            with open(self.config.STATUS_FILE,'w') as f:
                f.write(f"Validation status: {validation_status}")
                if missing_files:
                    f.write(f"\nMissing files: {missing_files}")
                    
            return validation_status
        except Exception as e:
            raise e