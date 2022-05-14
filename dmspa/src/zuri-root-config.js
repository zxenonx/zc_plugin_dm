import { registerApplication, start } from 'single-spa';

registerApplication({
    name: '@zuri/zuri-plugin-dm',
    app: () => System.import('@zuri/zuri-plugin-dm'),
    activeWhen: ['/'],
});

// registerApplication({
//   name: "@zuri/navbar",
//   app: () => System.import("@zuri/navbar"),
//   activeWhen: ["/"]
// });

start({
    urlRerouteOnly: true,
});
