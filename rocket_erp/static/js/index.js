import popper from "popper.js"
import $ from "jquery"
import toc from "toc"

$(document).ready(function() {
  // Открыть/закрыть меню на телефоне
  $("#burger-btn").on("click", function() {
    console.log(123);
    setTimeout(function() {
      $(".header-mobile-nav").removeClass("header-mobile-nav--hidden")
      $(".overlay").removeClass("overlay--hidden")
      $(".burger-toggle input").prop("checked", true)
    }, 500)
  })
  $("#close-mobile-nav").on("click", function() {
    $(".header-mobile-nav").addClass("header-mobile-nav--hidden")
    $(".overlay").addClass("overlay--hidden")
    $(".burger-toggle input").prop("checked", false)
  })
  // Показать/скрыть поиск
  $("#search-btn").on("click", function() {
    console.log(1)
    $(".header-right__nav").addClass("header-right__nav--hide")
    $(".header-right-btns__search").addClass("header-right-btns__search--active")
    $(this).addClass("header-right-btns__search-btn--hide")
  })
  $("#close-search-field").on("click", function() {
    $(".header-right__nav").removeClass("header-right__nav--hide")
    $(".header-right-btns__search").removeClass("header-right-btns__search--active")
    $(".header-right-btns__search-btn").removeClass("header-right-btns__search-btn--hide")
  })
  // Показать/скрыть левое меню на планшете
  $("#show-more").on("click", function() {
    $(".header-right__nav").toggleClass("header-right__nav--active")
  })

  // about-page TOC list
  const aboutPageContentHTML = $('#aboutTocSrc').html()
  if(aboutPageContentHTML) {
    const {headers} = toc.anchorize(aboutPageContentHTML)
    const processedHTML = toc.toc(headers, {
      header: '<h<%= level %><%= attrs %> id="<%= anchor %>"><%= header %></h<%= level %>>',
      TOC: '<div class="toc"><%= toc %></div>',
      openUL: '<ul data-depth="<%= depth %>">',
      closeUL: '</ul>',
      openLI: '<li data-level="H<%= level %>" class="toc-item"><a href="#<%= anchor %>"><%= text %></a>',
      closeLI: '</li>',
    })
    $('#aboutTocDest').html(processedHTML)
  }

  // Плавтная прокрутка к якорю по клику
  $('#aboutTocDest').on( 'click', 'a', function(){ 
    const el = $(this)
    const dest = el.attr('href')
    
    if(dest !== undefined && dest !== '' && /#\w/gi.test(dest)) {
      $('html').animate({ 
        scrollTop: $(dest).offset().top - 100
      }, 500)
    }
    return false;
  });

  // Подстветка активного пункта меню в "О фонде"
  const aboutContentBlocks = $('.page-about-content-block')
  const tocMenu = $('.toc')
  $(window).on('scroll', function () { // ОПТИМИЗИРОВАТЬ onScroll
    const position = $(this).scrollTop();
    const offset = 300

    aboutContentBlocks.each(function () {
      const top = $(this).offset().top - tocMenu.outerHeight() - offset
      const bottom = top + $(this).outerHeight() + offset;
      
      if (position >= top && position <= bottom) {
        tocMenu.find('a').removeClass('active');
        tocMenu.find(`a[href="#${ $(this).attr('id') }"]`).addClass('active');
      }
    });
  });
})
