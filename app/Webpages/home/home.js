angular.module("myApp.home", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/home', {
            templateUrl: 'Webpages/home/home.html',
            controller: 'homeController'
        });
    }])
    .controller('homeController', ['$scope', function($scope){ }]);