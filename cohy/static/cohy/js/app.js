var cohyApp = angular.module('cohyApp');

cohyApp.config(['$routeProvider','urls',
    function($routeProvider,urls){
        $routeProvider.
            when('/stations', {
                templateUrl : urls.station_list,
                controller : 'StationListCtrl'
            }).
            otherwise({
                redirectTo: '/home'
            });
    }
]);

cohyApp.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});
