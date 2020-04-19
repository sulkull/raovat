jQuery(document).ready(function($) {
				$('.click-hidden').click(function(event) {
					$('.show-hidden').slideToggle(300);
				});
				$('.list-color').click(function(event) {
					var dataimg = $(this).data('img').split(',');
					$('#img360').reel('images', dataimg);
				});
			});
			if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
				$("#img_01").elevateZoom({
					gallery:'gal1sss',
					zoomType: "lens",
					constrainType:"height",
					constrainSize:274,
					containLensZoom: true,
				});
			} else {
				$("#img_01").elevateZoom({
					gallery:'gal1sss',
					cursor: 'pointer',
					galleryActiveClass: 'active',
					imageCrossfade: true,
					responsive: true,
				    zoomWindowWidth:500,
				    zoomWindowHeight:300,
				    zoomWindowFadeIn: 500,
				    zoomWindowFadeOut: 750,
				    scrollZoom : true,
				    containLensZoom: true
				});
				$("#img_01").bind("click", function(e) {
				  	var ez =   $('#img_01').data('elevateZoom');
					$.fancybox(ez.getGalleryList());
				  	return false;
				});
			}