<template>
  <div>
    <TasksComponent />
  </div>
</template>

<script>
import TasksComponent from './components/Tasks.vue'

export default {
  name: 'App',
  components: { TasksComponent, }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
body{
  background-image: url('./assets/tasks.png');
  background-size: 100%;
  background-repeat: no-repeat;
  font-size: 13px;
  /* background-position: 0% 15%; */
}
</style>
