angular.module("myApp.invitations", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/invites', {
            templateUrl: 'Webpages/invitations/invitations.html',
            controller: 'invitationsController'
        });
    }])
    .controller("invitationsController", function($scope, $http) {
        $scope.username = localStorage.getItem('username');
        $scope.userid = localStorage.getItem('userid');

    });