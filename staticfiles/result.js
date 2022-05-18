function shareTwitter() {
  const sendText = "개발티콘"; // 전달할 텍스트
  const sendUrl = document.URL+'share/' // 전달할 URL
  window.open("https://twitter.com/intent/tweet?text=" + sendText + "&url=" + sendUrl)
}


function shareFacebook() {
  const sendUrl = document.URL+'share/' // 전달할 URL
  window.open("http://www.facebook.com/sharer/sharer.php?u=" + sendUrl)
}


function clipURL() {
  let url = ''
  let textarea = document.createElement("textarea")
  document.body.appendChild(textarea)
  url = document.URL
  textarea.value = url
  textarea.select()
  document.execCommand("copy")
  document.body.removeChild(textarea)
  swal({
    // swal html 태그 추가 후 클래스 입히기
    text: "url이 복사되었습니다.",
    timer: 1000,
    button: false,
    className: "swal-custom"
  })
}


function shareKakao() {
  // 사용할 앱의 JavaScript 키 설정
  Kakao.init('f5c01e33a60976edc933d00080bf4320')
  const resURL = document.URL

  // 카카오링크 버튼 생성
  Kakao.Link.createDefaultButton({
    container: '#btnKakao', // 카카오공유버튼ID
    objectType: 'feed',
    content: {
      title: "개발자 mbti", // 보여질 제목
      description: "당신이 개발자라면?", // 보여질 설명
      imageUrl: resURL, // 콘텐츠 URL
      link: {
          mobileWebUrl: resURL,
          webUrl: resURL,
      }
    }
  });
}
