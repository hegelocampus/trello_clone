<template>
  <div class="home">
    <TaskBoard />
  </div>
</template>

<script>
import TaskBoard from "@/components/TaskBoard.vue";

export default {
  name: "Home",
  components: {
    TaskBoard
  }
};
</script>
<style lang="scss">
.home {
  height: 100%;
  width: 100%;
}
</style>
