/**
 * @param {string} srcFolderId
 * @return {string[]} imgFolderIdArray
*/
function getFolderIdArray(srcFolderId){
  let imgFolderIdArray = [];
  const srcFolder = DriveApp.getFolderById(srcFolderId);
  let folders = srcFolder.getFolders();
  while(folders.hasNext()){
    folder = folders.next();
    imgFolderIdArray.push(folder.getId());
  }
  return imgFolderIdArray;
}

srcFolderId - "XXXXXXXXXXXXXXXXXXXXXXX";
id = getFolderIdArray(srcFolderId);
