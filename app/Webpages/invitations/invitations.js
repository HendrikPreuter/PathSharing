angular.module("myApp.invitations", ['ngRoute'])
    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/invites', {
            templateUrl: 'Webpages/invitations/invitations.html',
            controller: 'invitationsController'
        });
        $routeProvider.when('/create_invite', {
            templateUrl: 'Webpages/invitations/send_invitation.html',
            controller: 'sendInvitationsController'
        })
    }])
    .controller("invitationsController", function($scope, $http) {
        $scope.invites = [];
        console.log('anuskaas');
        $http.get('http://localhost:5000/invites').then(function(response) {
            $scope.invites = response.data;
        })

        $scope.accept_invite = function(invite_id, group_id, user_id) {
            data = {
                'invite_id': invite_id,
                'group_id': group_id,
                'user_id': user_id
            };
            $http.post('http://localhost:5000/accept_invite', data).then(function(response) {

            })
        }


    })
    .controller("sendInvitationsController", function($scope, $http) {
        $scope.send_invite = function(invitation) {
            data = {
                'group_name': invitation.group_name,
                'user_name': invitation.user_name
            }
            $http.post('http://localhost:5000/invites', data).then(function(reponse) {

            });
        }
    });