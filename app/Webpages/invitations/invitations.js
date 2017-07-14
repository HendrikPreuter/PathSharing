angular.module("myApp.invitations", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/invites', {
            templateUrl: 'Webpages/invitations/invitations.html',
            controller: 'invitationsController'
        })
    }])
    .controller("invitationsController", function($scope, $http) {
        if (!localStorage.getItem('token')) {
            window.location.href = '/#!login';
        }
        $http.get('http://localhost:5000/invites').then(function(response) {
            if(response.data.response === "error"){
                $scope.error = response.data.error;
            } else {
                $scope.invites = response.data;
            }
        });

        $scope.accept_invite = function(invite_id, group_id, user_id) {
            data = {
                'invite_id': invite_id,
                'group_id': group_id,
                'user_id': user_id
            };
            $http.post('http://localhost:5000/accept_invite', data).then(function(response) {
                if(response.data.response === "error"){
                    $scope.error = response.data.error;
                } else {
                    $scope.success = response.data.success;
                    location.reload();
                }
            })
        }
    });