import os
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            # If any column is not in schema → fail
            invalid_cols = [col for col in all_cols if col not in all_schema]
            validation_status = len(invalid_cols) == 0

            # Log results
            if validation_status:
                logger.info("All columns match schema.")
            else:
                logger.warning(f"Invalid columns found: {invalid_cols}")

            # Write clean status
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(str(validation_status))

            return validation_status

        except Exception as e:
            raise e
