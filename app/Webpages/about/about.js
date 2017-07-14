angular.module("myApp.about", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/about', {
            templateUrl: 'Webpages/about/about.html',
            controller: 'aboutController'
        });
    }])

    .controller("aboutController", function($scope, $http) {});
