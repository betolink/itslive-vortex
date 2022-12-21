import pkg_resources  # type: ignore

from itslive import data_cube as cubes

__all__ = ["cubes"]

__variables__ = [
    "acquisition_date_img1",
    "acquisition_date_img2",
    "autoRIFT_software_version",
    "chip_size_height",
    "chip_size_width",
    "date_center",
    "date_dt",
    "granule_url",
    "interp_mask",
    "mapping",
    "mid_date",
    "mission_img1",
    "mission_img2",
    "roi_valid_percentage",
    "satellite_img1",
    "satellite_img2",
    "sensor_img1",
    "sensor_img2",
    "stable_count_mask",
    "stable_count_slow",
    "stable_shift_flag",
    "v",
    "v_error",
    "va",
    "va_error",
    "va_error_mask",
    "va_error_modeled",
    "va_error_slow",
    "va_stable_shift",
    "va_stable_shift_mask",
    "va_stable_shift_slow",
    "vr",
    "vr_error",
    "vr_error_mask",
    "vr_error_modeled",
    "vr_error_slow",
    "vr_stable_shift",
    "vr_stable_shift_mask",
    "vr_stable_shift_slow",
    "vx",
    "vx_error",
    "vx_error_mask",
    "vx_error_modeled",
    "vx_error_slow",
    "vx_stable_shift",
    "vx_stable_shift_mask",
    "vx_stable_shift_slow",
    "vy",
    "vy_error",
    "vy_error_mask",
    "vy_error_modeled",
    "vy_error_slow",
    "vy_stable_shift",
    "vy_stable_shift_mask",
    "vy_stable_shift_slow",
    "x",
    "y",
]

# this comes from the installed version not the editable source
__version__ = pkg_resources.get_distribution("itslive").version
