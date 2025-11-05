/**
 * fieldBtn handler
 * get fields in the uv using uvId and ajax request
 * and add the response to=$('.uvfield-body')
 **/
function getFieldsInUv(uvId) {
  //making ajax request to=/student/filedInUv
  $.ajax({
    method: 'POST',
    url: '/student/filedInUv',
    data: { uvId: uvId },
    beforeSend: function () {
      //removeing prev added data
      $('.uvfield-body > tr').remove()
    },
    success: function (fields) {
      for (let i = 0; i < fields.length; i++) {
        var fieldsContent =
          '<tr><td>' + (i + 1) + '</td><td>' + fields[i] + '</td></tr>'

        //add field into the container
        $('.uvfield-body').append(fieldsContent)
      }
    },
  })
}

//fire getFieldsInUv on click to fieldBtn
$('.fieldBtn').click(function () {
  var uvId = $(this).data('uvid')
  getFieldsInUv(uvId)
})

/**
 * galleryBtn handler
 * get galleryPics in the uv using uvId and ajax request
 * and add the response to=$('.uvgallery-body')
 */
function getGalleryInUv(uvId) {
  //making ajax request to=/student/galleryInUv
  $.ajax({
    method: 'POST',
    url: '/student/galleryInUv',
    data: { uvId: uvId },
    beforeSend: function () {
      //empty pre req content from the gallery container
      $('.uvgallery-body > div').remove()
    },
    success: function (picName) {
      console.log(picName)
      for (let i = 0; i < picName.length; i++) {
        var galleryContent =
          '<div class="col-12 p-xs"><img class="w-full rounded" src="/static/./img/uv-gallery/' +
          picName[i] +
          '" alt=""/></div>'

        //add pic into the container
        $('.uvgallery-body').append(galleryContent)
      }
    },
  })
}

//fire getGalleryInUv on click to galleryBtn
$('.galleryBtn').click(function () {
  var uvId = $(this).data('uvid')
  getGalleryInUv(uvId)
})

/**
 * sendUp btn handler
 * sends up-table data into=/student/insertUp
 * shows processing loader and success dialog using sweet alert2
 */
function sendUp() {
  //num uv listed in the up-table
  var numUv = $('.upOrderNum').length
  //array to collect up-table data
  var upData = []

  //loop through each rows in the table
  for (let i = 0; i < numUv; i++) {
    //student id
    var stdId = $('#stdId').text()
    //university id
    uvId = $($('.upOrderNum')[i]).data('uvid').toString()
    //std given rank or orderer to the uv
    upOrder = $($('.upOrderNum')[i]).text()

    //add to the array
    upData[i] = [stdId, uvId, upOrder]
  }

  //making ajax post request
  $.ajax({
    method: 'POST',
    url: '/student/insertUp',
    data: { upData: JSON.stringify(upData) },
    beforeSend: function (res) {
      //while processing ajax req
      //showing swal loader
      Swal.fire({
        title: 'Please Wait !',
        html: 'we are uploading your up-data',
        allowOutsideClick: false,
        onBeforeOpen: () => {
          Swal.showLoading()
        },
      })
    },
    success: function (res) {
      //remove modal af 1500seconds
      setTimeout(function () {
        if (res == 'okay') {
          //on req success
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            html: 'Your up-data successfully uploaded',
            showConfirmButton: false,
            timer: 1500,
          })
        } else {
          //on req failed
          Swal.fire({
            position: 'top-end',
            icon: 'error',
            title: 'something went wrong!!!',
            showConfirmButton: false,
            timer: 1500,
          })
        }
      }, 1500)
    },
  })
}

//fire sendUp on click to sendUpBtn
$('#sendUp').click(function () {
  sendUp()
})

/**
 * exporting up-table data into image
 * using html2canvas plugin
 * show download popup modal using swa2
 */
function upTable2Img() {
  //get ub-table height for img height
  var imgHeight = $('#upTable').innerHeight()
  //get ub-table width for img width
  var imgWidth = $('#upTable').innerWidth()

  html2canvas(document.querySelector('#upTable'), {
    height: imgHeight,
    width: imgWidth,
  }).then(function (canvas) {
    //get imgUrl from data url of the canvas
    var imgUrl = encodeURI(canvas.toDataURL('image/png'))

    //show download popup modal using swa2
    Swal.fire({
      text: 'save ur up-table screenshot !!!',
      imageUrl: imgUrl,
      imageWidth: imgWidth,
      imageAlt: 'UP Table screenshot',
      showCancelButton: true,
      confirmButtonText: 'Save',
    }).then(function (res) {
      //if std click on save btn
      if (res.isConfirmed) {
        //downloading img as up-table-screenshot-<dateTime>.png form
        const date = new Date()
        image = document.createElement('a')
        image.download = 'up-table-screenshot-' + date.getTime() + '.png'
        image.href = imgUrl
        image.click()
      }
    })
  })
}

//fire upTable2Img on click to exportUp
$('#exportUp').click(function () {
  //showing loader on process
  Swal.fire({
    title: 'Please Wait !',
    html: 'converting up-table data into image...',
    allowOutsideClick: false,
    onBeforeOpen: () => {
      Swal.showLoading()
    },
  })

  //fire the func af 1000second b/c in order to show loader popup
  setTimeout(upTable2Img(), 1000)
})

/**
 * after drag and drop ordering uv list the order num
 *  is incorrect
 * */
function updateTheOrderNum() {
  //getting total list of uv
  totalListItem = $('.table tbody tr').length
  //reordering the order of uv list
  for (var i = 1; i <= 4; i++) {
    $('.table tbody tr:nth-child(' + i + ') td > .upOrderNum').text(i)
  }
}

//order the num
updateTheOrderNum()

// Sortable rows
$('#upOrderTable tbody').sortable({
  update: function (eve, ui) {
    //on Finished sorting uv update the order number
    updateTheOrderNum()
  },
})
