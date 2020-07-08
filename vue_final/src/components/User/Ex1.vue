<template>
  <div>
    <el-col :span="5">
    <p >请填写正确的开关顺序:</p>
    <el-input v-model = "order" type = "primary" id = "order" ></el-input></el-col>
    <el-button type="primary" id="submit" icon="el-icon-d-arrow-right" @click="submit(order)">submit</el-button>
  </div>
</template>

<script>
  export default {
    name: "score",
    data() {
      return {
        order: "",
        score: '0',
        formLabelWidth: "100px"
      };
    },
    created() {
     
    },
    methods: {
      submit(order) {
        if(order ==='123')
          this.score = '100'
        this.$axios
          .get(this.HOME + "/api/ex_score", {
            params: {
              eid: '2',
              uloginid: this.Global.loginid,
              uscore: this.score,
            }
          })
        this.$router.push({ path: "/User/Experiment" });
    }}
  };
</script>

<style lang="scss" scoped>
  #submit{
    position: absolute;
    top: 100px;
    left: 10px;
  }
  .button {
    background: transparent;
    color: transparent;
    position: absolute;
    margin-top: 500px;
    margin-bottom: 500px;
    margin-left: 45%;
    padding-left: 0%;
    padding-right: 0%;
    padding-left: -5px;
    padding-right: 6%;
  }
</style>
