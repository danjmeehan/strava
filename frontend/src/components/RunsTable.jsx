[plugin:vite:import-analysis] Failed to resolve import "./components/RunsTable" from "src/App.jsx". Does the file exist?
/Users/danjmeehan/Documents/Training/strava/frontend/src/App.jsx:4:22
19 |  import axios from "axios";
20 |  import WeeklyMileageChart from "./components/WeeklyMileageChart";
21 |  import RunsTable from "./components/RunsTable";
   |                         ^
22 |  import "./App.css";
23 |  function App() {
    at TransformPluginContext._formatError (file:///Users/danjmeehan/Documents/Training/strava/frontend/node_modules/vite/dist/node/chunks/dep-C6qYk3zB.js:47149:41)
    at TransformPluginContext.error (file:///Users/danjmeehan/Documents/Training/strava/frontend/node_modules/vite/dist/node/chunks/dep-C6qYk3zB.js:47144:16)
    at normalizeUrl (file:///Users/danjmeehan/Documents/Training/strava/frontend/node_modules/vite/dist/node/chunks/dep-C6qYk3zB.js:45414:23)
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async file:///Users/danjmeehan/Documents/Training/strava/frontend/node_modules/vite/dist/node/chunks/dep-C6qYk3zB.js:45533:39
    at async Promise.all (index 6)
    at async TransformPluginContext.transform (file:///Users/danjmeehan/Documents/Training/strava/frontend/node_modules/vite/dist/node/chunks/dep-C6qYk3zB.js:45460:7)
    at async EnvironmentPluginContainer.transform (file:///Users/danjmeehan/Documents/Training/strava/frontend/node_modules/vite/dist/node/chunks/dep-C6qYk3zB.js:46992:18)
    at async loadAndTransform (file:///Users/danjmeehan/Documents/Training/strava/frontend/node_modules/vite/dist/node/chunks/dep-C6qYk3zB.js:40833:27
