var cohyApp = angular.module('cohyApp');

cohyApp.config(['$routeProvider','urls',
    function($routeProvider,urls){
        $routeProvider.
            when('/stations', {
                templateUrl : urls.station_list,
                controller : 'StationListCtrl'
            }).
            when('/station/new', {
                templateUrl : urls.station_new,
                controller : 'StationNewCtrl'
            }).
            when('/home', {
                templateUrl : urls.home,
                controller : 'HomeCtrl'
            }).
            otherwise({
                redirectTo: '/home'
            });
    }
]);

cohyApp.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
