from dataclasses import dataclass
from pathlib import Path

# define dataclass and inside that give parameter (frozen=True) and inside dacorator define class DataIngestion
@dataclass(frozen=True) # inside data class we can mention our varibles , and what is the type of varible
class DataIngestionConfig:
    root_dir: Path # variable : type of varibale is Path
    source_URL: str
    local_data_file:Path
    unzip_dir:Path



@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path 
