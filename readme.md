# ![alt text](/docs/assets/logo48.png "StickerAutomation") StickerAutomation
_Automated generation of stickers packs compatible with [Sticker maker for WhatsApp](https://getstickerpack.com/)._

## Setup
- Clone this template repository
- Fill the `src/` folder with sticker packs, please see `src/readme.md` for more info about the packs
- Set up a release method in the build script, `build.py`. An example that create a Github release in your repo is provided.
- Commit these to the `development` branch for running automated tests
- Complete a pull request to `release` and await automated build
- Publish the new version of your pack

## Tools
- Github Actions
- Python