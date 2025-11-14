from kagglesdk.competitions.types.competition_api_service import *
import io
import types
from ..models.dataset_column import DatasetColumn as DatasetColumn
from ..models.upload_file import UploadFile as UploadFile
from _typeshed import Incomplete
from kaggle.configuration import Configuration as Configuration
from kaggle.models.kaggle_models_extended import (
    File as File,
    Kernel as Kernel,
    ResumableUploadResult as ResumableUploadResult,
)
from kagglesdk.datasets.types.dataset_api_service import (
    ApiListDatasetFilesResponse as ApiListDatasetFilesResponse,
)
from kagglesdk.kernels.types.kernels_api_service import (
    ApiSaveKernelResponse as ApiSaveKernelResponse,
)

class DirectoryArchive:
    name: Incomplete
    path: Incomplete
    def __init__(self, fullpath, format) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args) -> None: ...

class ResumableUploadContext:
    no_resume: Incomplete
    def __init__(self, no_resume: bool = False) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        exc_traceback: types.TracebackType | None,
    ) -> None: ...
    def get_upload_info_file_path(self, path): ...
    def new_resumable_file_upload(self, path, start_blob_upload_request): ...

class ResumableFileUpload:
    RESUMABLE_UPLOAD_EXPIRY_SECONDS: Incomplete
    path: Incomplete
    start_blob_upload_request: Incomplete
    context: Incomplete
    timestamp: Incomplete
    start_blob_upload_response: Incomplete
    can_resume: bool
    upload_complete: bool
    def __init__(self, path, start_blob_upload_request, context) -> None: ...
    def get_token(self): ...
    def load(self) -> None: ...
    def upload_initiated(self, start_blob_upload_response) -> None: ...
    def upload_completed(self) -> None: ...
    def cleanup(self) -> None: ...
    def to_dict(self): ...
    def from_dict(other, context): ...
    def to_str(self): ...

class KaggleApi:
    __version__: str
    CONFIG_NAME_PROXY: str
    CONFIG_NAME_COMPETITION: str
    CONFIG_NAME_PATH: str
    CONFIG_NAME_USER: str
    CONFIG_NAME_KEY: str
    CONFIG_NAME_SSL_CA_CERT: str
    HEADER_API_VERSION: str
    DATASET_METADATA_FILE: str
    OLD_DATASET_METADATA_FILE: str
    KERNEL_METADATA_FILE: str
    MODEL_METADATA_FILE: str
    MODEL_INSTANCE_METADATA_FILE: str
    MAX_NUM_INBOX_FILES_TO_UPLOAD: int
    MAX_UPLOAD_RESUME_ATTEMPTS: int
    config_dir: Incomplete
    config_file: str
    config: Incomplete
    config_values: Incomplete
    already_printed_version_warning: bool
    args: Incomplete
    valid_push_kernel_types: Incomplete
    valid_push_language_types: Incomplete
    valid_push_pinning_types: Incomplete
    valid_list_languages: Incomplete
    valid_list_kernel_types: Incomplete
    valid_list_output_types: Incomplete
    valid_list_sort_by: Incomplete
    valid_competition_groups: Incomplete
    valid_competition_categories: Incomplete
    valid_competition_sort_by: Incomplete
    valid_dataset_file_types: Incomplete
    valid_dataset_license_names: Incomplete
    valid_dataset_sort_bys: Incomplete
    valid_model_sort_bys: Incomplete
    command_prefixes_allowing_anonymous_access: Incomplete
    competition_fields: Incomplete
    submission_fields: Incomplete
    competition_file_fields: Incomplete
    competition_file_labels: Incomplete
    competition_leaderboard_fields: Incomplete
    dataset_fields: Incomplete
    dataset_labels: Incomplete
    dataset_file_fields: Incomplete
    model_fields: Incomplete
    model_all_fields: Incomplete
    model_file_fields: Incomplete
    def with_retry(
        self,
        func,
        max_retries: int = 10,
        initial_delay_millis: int = 500,
        retry_multiplier: float = 1.7,
        randomness_factor: float = 0.5,
    ): ...
    def authenticate(self) -> None: ...
    def read_config_environment(self, config_data=None, quiet: bool = False): ...
    def read_config_file(self, config_data=None, quiet: bool = False): ...
    def set_config_value(self, name, value, quiet: bool = False) -> None: ...
    def unset_config_value(self, name, quiet: bool = False) -> None: ...
    def get_config_value(self, name): ...
    def get_default_download_dir(self, *subdirs): ...
    def print_config_value(
        self, name, prefix: str = "- ", separator: str = ": "
    ) -> None: ...
    def print_config_values(self, prefix: str = "- ") -> None: ...
    def build_kaggle_client(self): ...
    def camel_to_snake(self, name): ...
    def lookup_enum(self, enum_class, item_name): ...
    def short_enum_name(self, value): ...
    def competitions_list(
        self, group=None, category=None, sort_by=None, page: int = 1, search=None
    ): ...
    def competitions_list_cli(
        self,
        group=None,
        category=None,
        sort_by=None,
        page: int = 1,
        search=None,
        csv_display: bool = False,
    ) -> None: ...
    def competition_submit_code(
        self,
        file_name,
        message,
        competition,
        kernel=None,
        kernel_version=None,
        quiet: bool = False,
    ): ...
    def competition_submit(
        self, file_name, message, competition, quiet: bool = False
    ): ...
    def competition_submit_cli(
        self,
        file_name=None,
        message=None,
        competition=None,
        kernel=None,
        version=None,
        competition_opt=None,
        quiet: bool = False,
    ): ...
    def competition_submissions(
        self,
        competition,
        group=None,
        sort=None,
        page_token: int = 0,
        page_size: int = 20,
    ): ...
    def competition_submissions_cli(
        self,
        competition=None,
        competition_opt=None,
        csv_display: bool = False,
        page_token=None,
        page_size: int = 20,
        quiet: bool = False,
    ) -> None: ...
    def competition_list_files(
        self, competition, page_token=None, page_size: int = 20
    ): ...
    def competition_list_files_cli(
        self,
        competition,
        competition_opt=None,
        csv_display: bool = False,
        page_token=None,
        page_size: int = 20,
        quiet: bool = False,
    ) -> None: ...
    def competition_download_file(
        self,
        competition,
        file_name,
        path=None,
        force: bool = False,
        quiet: bool = False,
    ) -> None: ...
    def competition_download_files(
        self, competition, path=None, force: bool = False, quiet: bool = True
    ) -> None: ...
    def competition_download_cli(
        self,
        competition,
        competition_opt=None,
        file_name=None,
        path=None,
        force: bool = False,
        quiet: bool = False,
    ) -> None: ...
    def competition_leaderboard_download(
        self, competition, path, quiet: bool = True
    ) -> None: ...
    def competition_leaderboard_view(self, competition): ...
    def competition_leaderboard_cli(
        self,
        competition,
        competition_opt=None,
        path=None,
        view: bool = False,
        download: bool = False,
        csv_display: bool = False,
        quiet: bool = False,
    ) -> None: ...
    def dataset_list(
        self,
        sort_by=None,
        size=None,
        file_type=None,
        license_name=None,
        tag_ids=None,
        search=None,
        user=None,
        mine: bool = False,
        page: int = 1,
        max_size=None,
        min_size=None,
    ): ...
    def dataset_list_cli(
        self,
        sort_by=None,
        size=None,
        file_type=None,
        license_name=None,
        tag_ids=None,
        search=None,
        user=None,
        mine: bool = False,
        page: int = 1,
        csv_display: bool = False,
        max_size=None,
        min_size=None,
    ) -> None: ...
    def dataset_metadata_prep(self, dataset, path): ...
    def dataset_metadata_update(self, dataset, path) -> None: ...
    def dataset_metadata(self, dataset, path): ...
    def dataset_metadata_cli(self, dataset, path, update, dataset_opt=None) -> None: ...
    def dataset_list_files(self, dataset, page_token=None, page_size: int = 20): ...
    def dataset_list_files_cli(
        self,
        dataset,
        dataset_opt=None,
        csv_display: bool = False,
        page_token=None,
        page_size: int = 20,
    ) -> None: ...
    def dataset_status(self, dataset): ...
    def dataset_status_cli(self, dataset, dataset_opt=None): ...
    def dataset_download_file(
        self,
        dataset,
        file_name,
        path=None,
        force: bool = False,
        quiet: bool = True,
        licenses=[],
    ): ...
    def dataset_download_files(
        self,
        dataset,
        path=None,
        force: bool = False,
        quiet: bool = True,
        unzip: bool = False,
        licenses=[],
    ) -> None: ...
    def dataset_download_cli(
        self,
        dataset,
        dataset_opt=None,
        file_name=None,
        path=None,
        unzip: bool = False,
        force: bool = False,
        quiet: bool = False,
    ) -> None: ...
    def dataset_create_version(
        self,
        folder,
        version_notes,
        quiet: bool = False,
        convert_to_csv: bool = True,
        delete_old_versions: bool = False,
        dir_mode: str = "skip",
    ): ...
    def dataset_create_version_cli(
        self,
        folder,
        version_notes,
        quiet: bool = False,
        convert_to_csv: bool = True,
        delete_old_versions: bool = False,
        dir_mode: str = "skip",
    ) -> None: ...
    def dataset_initialize(self, folder): ...
    def dataset_initialize_cli(self, folder=None) -> None: ...
    def dataset_create_new(
        self,
        folder,
        public: bool = False,
        quiet: bool = False,
        convert_to_csv: bool = True,
        dir_mode: str = "skip",
    ): ...
    def dataset_create_new_cli(
        self,
        folder=None,
        public: bool = False,
        quiet: bool = False,
        convert_to_csv: bool = True,
        dir_mode: str = "skip",
    ) -> None: ...
    def download_file(
        self,
        response,
        outfile,
        http_client,
        quiet: bool = True,
        resume: bool = False,
        chunk_size: int = 1048576,
    ) -> None: ...
    def kernels_list(
        self,
        page: int = 1,
        page_size: int = 20,
        dataset=None,
        competition=None,
        parent_kernel=None,
        search=None,
        mine: bool = False,
        user=None,
        language=None,
        kernel_type=None,
        output_type=None,
        sort_by=None,
    ): ...
    def kernels_list_cli(
        self,
        mine: bool = False,
        page: int = 1,
        page_size: int = 20,
        search=None,
        csv_display: bool = False,
        parent=None,
        competition=None,
        dataset=None,
        user=None,
        language=None,
        kernel_type=None,
        output_type=None,
        sort_by=None,
    ) -> None: ...
    def kernels_list_files(self, kernel, page_token=None, page_size: int = 20): ...
    def kernels_list_files_cli(
        self,
        kernel,
        kernel_opt=None,
        csv_display: bool = False,
        page_token=None,
        page_size: int = 20,
    ) -> None: ...
    def kernels_initialize(self, folder): ...
    def kernels_initialize_cli(self, folder=None) -> None: ...
    def kernels_push(self, folder, timeout=None) -> ApiSaveKernelResponse: ...
    def kernels_push_cli(self, folder, timeout) -> None: ...
    def kernels_pull(
        self, kernel, path, metadata: bool = False, quiet: bool = True
    ): ...
    def kernels_pull_cli(
        self, kernel, kernel_opt=None, path=None, metadata: bool = False
    ) -> None: ...
    def kernels_output(self, kernel, path, force: bool = False, quiet: bool = True): ...
    def kernels_output_cli(
        self,
        kernel,
        kernel_opt=None,
        path=None,
        force: bool = False,
        quiet: bool = False,
    ) -> None: ...
    def kernels_status(self, kernel): ...
    def kernels_status_cli(self, kernel, kernel_opt=None) -> None: ...
    def model_get(self, model): ...
    def model_get_cli(self, model, folder=None) -> None: ...
    def model_list(
        self,
        sort_by=None,
        search=None,
        owner=None,
        page_size: int = 20,
        page_token=None,
    ): ...
    def model_list_cli(
        self,
        sort_by=None,
        search=None,
        owner=None,
        page_size: int = 20,
        page_token=None,
        csv_display: bool = False,
    ) -> None: ...
    def model_initialize(self, folder): ...
    def model_initialize_cli(self, folder=None) -> None: ...
    def model_create_new(self, folder): ...
    def model_create_new_cli(self, folder=None) -> None: ...
    def model_delete(self, model, yes): ...
    def model_delete_cli(self, model, yes) -> None: ...
    def model_update(self, folder): ...
    def model_update_cli(self, folder=None) -> None: ...
    def model_instance_get(self, model_instance): ...
    def model_instance_get_cli(self, model_instance, folder=None) -> None: ...
    def model_instance_initialize(self, folder): ...
    def model_instance_initialize_cli(self, folder) -> None: ...
    def model_instance_create(
        self, folder, quiet: bool = False, dir_mode: str = "skip"
    ): ...
    def model_instance_create_cli(
        self, folder, quiet: bool = False, dir_mode: str = "skip"
    ) -> None: ...
    def model_instance_delete(self, model_instance, yes): ...
    def model_instance_delete_cli(self, model_instance, yes) -> None: ...
    def model_instance_files(
        self,
        model_instance,
        page_token=None,
        page_size: int = 20,
        csv_display: bool = False,
    ): ...
    def model_instance_files_cli(
        self,
        model_instance,
        page_token=None,
        page_size: int = 20,
        csv_display: bool = False,
    ) -> None: ...
    def model_instance_update(self, folder): ...
    def model_instance_update_cli(self, folder=None) -> None: ...
    def model_instance_version_create(
        self,
        model_instance,
        folder,
        version_notes: str = "",
        quiet: bool = False,
        dir_mode: str = "skip",
    ): ...
    def model_instance_version_create_cli(
        self,
        model_instance,
        folder,
        version_notes: str = "",
        quiet: bool = False,
        dir_mode: str = "skip",
    ) -> None: ...
    def model_instance_version_download(
        self,
        model_instance_version,
        path=None,
        force: bool = False,
        quiet: bool = True,
        untar: bool = False,
    ): ...
    def model_instance_version_download_cli(
        self,
        model_instance_version,
        path=None,
        untar: bool = False,
        force: bool = False,
        quiet: bool = False,
    ): ...
    def model_instance_version_files(
        self,
        model_instance_version,
        page_token=None,
        page_size: int = 20,
        csv_display: bool = False,
    ): ...
    def model_instance_version_files_cli(
        self,
        model_instance_version,
        page_token=None,
        page_size: int = 20,
        csv_display: bool = False,
    ) -> None: ...
    def model_instance_version_delete(self, model_instance_version, yes): ...
    def model_instance_version_delete_cli(
        self, model_instance_version, yes
    ) -> None: ...
    def files_upload_cli(
        self, local_paths, inbox_path, no_resume, no_compress
    ) -> None: ...
    def file_upload_cli(self, local_path, inbox_path, no_compress, upload_context): ...
    def print_obj(self, obj, indent: int = 2) -> None: ...
    def download_needed(self, response, outfile, quiet: bool = True): ...
    def print_table(self, items, fields, labels=None) -> None: ...
    def print_csv(self, items, fields, labels=None) -> None: ...
    def string(self, item): ...
    def get_or_fail(self, data, key): ...
    def get_or_default(self, data, key, default): ...
    def get_bool(self, data, key, default): ...
    def set_if_present(self, data, key, output, output_key) -> None: ...
    def get_dataset_metadata_file(self, folder): ...
    def get_model_metadata_file(self, folder): ...
    def get_model_instance_metadata_file(self, folder): ...
    def process_response(self, result): ...
    def is_up_to_date(self, server_version): ...
    def upload_files(
        self,
        request,
        resources,
        folder,
        blob_type,
        upload_context,
        quiet: bool = False,
        dir_mode: str = "skip",
    ) -> None: ...
    def process_column(self, column): ...
    def upload_complete(self, path, url, quiet, resume: bool = False): ...
    def validate_dataset_string(self, dataset) -> None: ...
    def split_dataset_string(self, dataset): ...
    def validate_model_string(self, model) -> None: ...
    def split_model_string(self, model): ...
    def validate_model_instance_string(self, model_instance) -> None: ...
    def split_model_instance_string(self, model_instance): ...
    def validate_model_instance_version_string(
        self, model_instance_version
    ) -> None: ...
    def validate_kernel_string(self, kernel) -> None: ...
    def validate_model_string(self, model) -> None: ...
    def validate_resources(self, folder, resources) -> None: ...
    def validate_files_exist(self, folder, resources) -> None: ...
    def validate_no_duplicate_paths(self, resources) -> None: ...
    def convert_to_dataset_file_metadata(self, file_data, path): ...
    def validate_date(self, date) -> None: ...
    def sanitize_markdown(self, markdown): ...
    def confirmation(self): ...

class TqdmBufferedReader(io.BufferedReader):
    progress_bar: Incomplete
    def __init__(self, raw, progress_bar) -> None: ...
    def read(self, *args, **kwargs): ...
    def increment(self, length) -> None: ...

class FileList:
    error_message: str
    files: Incomplete
    nextPageToken: Incomplete
    def __init__(self, init_dict) -> None: ...
    @staticmethod
    def from_response(response) -> None: ...

def attributes(obj): ...
def print_attributes(obj) -> None: ...
