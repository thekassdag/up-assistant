//dataTable
$('#stdListTable').DataTable()
$('#naturalStdUPDataListTable').DataTable()
$('#socialStdUPDataListTable').DataTable()

//open import stdList excel file uploading window
function importStdData() {
  Swal.fire({
    title: '<h3>Import Student List</h3>',
    html:
      '<form method="post" id="importStdList" action="/admin/importStdList" enctype="multipart/form-data" ><div class="import-form"><i class=" fa-solid fa-file-excel">excel file</i><input type="file" class=" form-control" required id="stdListFile" name="stdListData" accept=".csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/vnd.ms-excel" /><input class="d-none" id="importStdListFormBtn" type="submit"></div></form>',
    showCloseButton: true,
    showCancelButton: true,
    confirmButtonText: 'Import',
    cancelButtonText: 'cancel',
  }).then(function (result) {
    if (result.isConfirmed && $('#stdListFile').val() != '') {
      //on click redi to '/importStdList'
      $('#importStdListFormBtn').trigger('click')
    } else if (result.isConfirmed) {
      Swal.fire({
        position: 'top-end',
        icon: 'error',
        text: 'import student list data filed is required!!',
        showConfirmButton: false,
        timer: 1700,
      })
    }
  })
}
$('#importStudentData').click(function () {
  setTimeout(importStdData(), 1000)
})

function exportUPData(stream) {
  $.ajax({
    url: '/admin/exportUPData/' + stream + '',
    method: 'post',
    beforeSend: function () {
      Swal.fire({
        title: 'Please Wait !',
        html: 'Exporting students up-data',
        allowOutsideClick: false,
        onBeforeOpen: () => {
          Swal.showLoading()
        },
      })
    },
    success: function (fileName) {
      exportedFile = document.createElement('a')
      exportedFile.download = fileName
      exportedFile.href = '/static/download/' + fileName
      exportedFile.click()
      Swal.close()
    },
  })
}

$('#export-social-std').click(function () {
  exportUPData('S')
})
$('#export-natural-std').click(function () {
  exportUPData('N')
})
