$(document).ready(function() {

  console.log('nav ready');

  $(".switch").click(function() {
    $(".login-form").toggle()
    $(".signup-form").toggle()
  })
  $(".register").click(function() {
    $(".login-signup").css({
      'visibility': 'visible'
    })
  })
  $(".login-signup").click(function() {
    $(this).parent().css({
      'visibility': 'hidden'
    })
  })
  $(".profile img").mouseover(function() {
    $(".items").fadeIn()

  })
  $(".items").mouseleave(function() {
    $(this).fadeOut()
  })
  $(".profile").mouseleave(function() {
    $(".items").fadeOut()
  })
  if ($(window).width() < 767){
    $(".profile").hide()
    $(".site").hide()
    $(".r-top").hide()
    $(".r-bottom").hide()
  }else{
    $(".profile").show()
    $(".site").show()
    $(".r-top").show()
    $(".r-bottom").show()
  }
$(window).on('resize',function(){
  winWidth=$(this).width()
  if (winWidth <776){
    $(".profile").hide()
    $(".site").hide()
    $(".r-top").hide()
    $(".r-bottom").hide()
  }else{
    $(".profile").show()
    $(".site").show()
    $(".r-top").show()
    $(".r-bottom").show()

}
})
$(window).on('scroll',function(){
  if($(this).scrollTop() >100){
    console.log('greater');
    $("#logo-w2").hide()
    $("#logo-w3").hide()
    $("#logo-a1").hide()
    $("#logo-a2").hide()
    $("#logo-r").hide()
    $("#logo-d").hide()
    $("#logo-s").hide()
  }else{
    $("#logo-w2").show()
    $("#logo-w3").show()
    $("#logo-a1").show()
    $("#logo-a2").show()
    $("#logo-r").show()
    $("#logo-d").show()
    $("#logo-s").show()
  }
})
$(".cancel").click(function(){
  $(".search-input").hide()
  $(".logo").show()
  if ($(window).width() > 767){
    $(".profile").show()
    $(".site").show()
  }
  $(".search").show()
})
$(".search").click(function(){
  $(".logo").hide()
  $(".profile").hide()
  $(".site").hide()
  $(this).hide()
  $(".search-input").show()
})
})
