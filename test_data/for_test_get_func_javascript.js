/**
 * @param {string} srcFolderId
 * @return {string[]} imgFolderIdArray
 */
function getFolderIdArray(srcFolderId) {
  let imgFolderIdArray = [];
  const srcFolder = DriveApp.getFolderById(srcFolderId);
  let folders = srcFolder.getFolders();
  while (folders.hasNext()) {
    folder = folders.next();
    imgFolderIdArray.push(folder.getId());
  }
  return imgFolderIdArray;
}

function testtest() {
  return true;
}

function main() {
  let tmpId = "ZZZZZZZZZZZZZZZZZZZZZZZZZZz";
  let idArray = getFolderIdArray(tmpId);
}

let srcFolderId = "XXXXXXXXXXXXXXXXXXXXXXX";
let id = getFolderIdArray(srcFolderId);
srcFolderId = "YYYYYYYYYYYYYYYYYYYYYYYYY";
id = getFolderIdArray(srcFolderId);
