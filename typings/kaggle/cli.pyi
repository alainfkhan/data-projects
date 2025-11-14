from _typeshed import Incomplete
from kaggle import KaggleApi as KaggleApi, api as api

ApiException = IOError

def main() -> None: ...
def parse_competitions(subparsers) -> None: ...
def parse_datasets(subparsers) -> None: ...
def parse_kernels(subparsers) -> None: ...
def parse_models(subparsers) -> None: ...
def parse_model_instances(subparsers) -> None: ...
def parse_model_instance_versions(subparsers) -> None: ...
def parse_files(subparsers) -> None: ...
def parse_config(subparsers) -> None: ...

class Help:
    kaggle_choices: Incomplete
    competitions_choices: Incomplete
    datasets_choices: Incomplete
    kernels_choices: Incomplete
    models_choices: Incomplete
    model_instances_choices: Incomplete
    model_instance_versions_choices: Incomplete
    files_choices: Incomplete
    config_choices: Incomplete
    kaggle: Incomplete
    group_competitions: str
    group_datasets: str
    group_kernels: str
    group_models: str
    group_model_instances: str
    group_model_instance_versions: str
    group_files: str
    group_config: str
    command_competitions_list: str
    command_competitions_files: str
    command_competitions_download: str
    command_competitions_submit: str
    command_competitions_submissions: str
    command_competitions_leaderboard: str
    command_datasets_list: str
    command_datasets_files: str
    command_datasets_download: str
    command_datasets_new: str
    command_datasets_new_version: str
    command_datasets_init: str
    command_datasets_metadata: str
    command_datasets_status: str
    command_kernels_list: str
    command_kernels_files: str
    command_kernels_init: str
    command_kernels_push: str
    command_kernels_pull: str
    command_kernels_output: str
    command_kernels_status: str
    command_models_files: str
    command_models_get: str
    command_models_list: str
    command_models_init: str
    command_models_new: str
    command_models_delete: str
    command_models_update: str
    command_files_upload: str
    command_config_path: str
    command_config_proxy: str
    command_config_competition: str
    command_config_view: str
    command_config_set: str
    command_config_unset: str
    param_downfolder: str
    param_wp: str
    param_proxy: str
    param_quiet: str
    param_public: str
    param_keep_tabular: str
    param_dir_mode: str
    param_delete_old_version: str
    param_force: str
    param_upfile: str
    param_code_kernel: str
    param_code_version: str
    param_csv: str
    param_page: str
    param_page_size: str
    param_page_token: str
    param_search: str
    param_mine: str
    param_unzip: str
    param_untar: str
    param_yes: str
    param_competition: str
    param_competition_nonempty: str
    param_competition_leaderboard_view: str
    param_competition_leaderboard_download: str
    param_competition_file: str
    param_competition_message: str
    param_competition_group: str
    param_competition_category: str
    param_competition_sort_by: str
    param_dataset: str
    param_dataset_file: str
    param_dataset_version_notes: str
    param_dataset_upfile: str
    param_dataset_sort_by: str
    param_dataset_size: str
    param_dataset_file_type: str
    param_dataset_license: str
    param_dataset_tags: str
    param_dataset_user: str
    param_dataset_metadata_dir: str
    param_dataset_metadata_update: str
    param_dataset_maxsize: str
    param_dataset_minsize: str
    param_kernel: str
    param_kernel_init: str
    param_kernel_upfile: str
    param_kernel_parent: str
    param_kernel_competition: str
    param_kernel_dataset: str
    param_kernel_timeout: str
    param_kernel_user: str
    param_kernel_language: str
    param_kernel_type: str
    param_kernel_output_type: str
    param_kernel_sort_by: str
    param_kernel_pull_metadata: str
    param_model: str
    param_model_sort_by: str
    param_model_owner: str
    param_model_downfile: str
    param_model_upfile: str
    param_model_instance: str
    command_model_instances_get: str
    command_model_instances_init: str
    command_model_instances_files: str
    command_model_instances_new: str
    param_model_instance_downfile: str
    param_model_instance_upfile: str
    command_model_instances_delete: str
    command_model_instances_update: str
    param_model_instance_version: str
    command_model_instance_versions_new: str
    param_model_instance_version_upfile: str
    command_model_instance_versions_delete: str
    command_model_instance_versions_download: str
    command_model_instance_versions_files: str
    param_model_instance_version_notes: str
    param_files_upload_inbox_path: str
    param_files_upload_local_paths: str
    param_files_upload_no_compress: str
    param_files_upload_no_resume: str
    param_config_name: str
    param_config_value: Incomplete
