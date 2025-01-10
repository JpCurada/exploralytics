# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2024-01-10

### Changed
- Reorganized package structure to use src layout
- Updated package dependencies
- Improved import structure
- Added ReadTheDocs documentation support

### Fixed
- Fixed package installation issues
- Corrected module imports
- Improved package discoverability

## [1.0.0] - 2025-01-09

### Added
- New visualization methods:
  - `plot_correlation_map()` for creating correlation matrix heatmaps
  - `plot_correlation_with_target()` for analyzing feature correlations with a target variable
  - `plot_dot()` for creating dot plots with connecting lines
  - `plot_hbar()` for creating horizontal bar charts with highlighting options
- Customizable highlighting options for top and bottom values
- Support for reference lines and statistics (mean, median)
- Enhanced hover information with detailed tooltips
- Flexible styling options including font customization
- Footer support for all plot types

### Changed
- Migrated from setup.py to pyproject.toml
- Added GitHub Actions for automated deployment
- Updated minimum Python requirement to 3.9
- Improved plot styling and configuration options
- Enhanced documentation and examples

### Fixed
- Improved handling of missing values in correlation plots
- Better handling of categorical data in histograms
- Enhanced axis formatting and label positioning

## [0.1.0] - 2024
- Initial release with basic plotting functionality
- Basic histogram and correlation plotting
- Simple customization options

[1.0.1]: https://github.com/jpcurada/exploralytics/releases/tag/v1.0.1
[1.0.0]: https://github.com/jpcurada/exploralytics/releases/tag/v1.0.0
[0.1.0]: https://github.com/jpcurada/exploralytics/releases/tag/v0.1.0