angular.module('Falcon-email')
	.directive('renderPreview', function () {
		 return {
		 	scope: {
		 		html: '='
		 	},
		 	templateUrl: '/static/js/renderPreview/renderPreview.directive.html',
		 	link: function (scope, element) {
		 		scope.$watch('html', function( val ) {
		 				element.html(val);
		 		});
		 	}
		 }		
	});