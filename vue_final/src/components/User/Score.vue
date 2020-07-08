<template>
  <div>
    <el-col :span="5">
    <el-input v-model = "pwd" type = "password" id = "pwd" ></el-input>
    <el-input v-model = "uloginid" type = "password" id = "uloginid" ></el-input>
    <el-input v-model = "uscore" type = "password" id = "uscore" ></el-input></el-col>
    <el-button type="primary" icon="el-icon-d-arrow-right" id = "submit" @click="submit(pwd,uloginid,uscore)">submit</el-button>
  </div>
</template>

<script>
  export default {
    name: "score",
    data() {
      return {
        pwd: "",
        uloginid: "",
        uscore: "",
        formLabelWidth: "100px"
      };
    },
    created() {

    },
    methods: {
      submit(pwd, uloginid, uscore) {
        this.$axios
          .get(this.HOME + "/api/car_score", {
            params: {
              pwd: pwd,
              uloginid: uloginid,
              uscore: uscore
            }
          })
          .then(response=>{console.log(response.data.msg)});
        this.$router.push({ path: "/User/Experiment" });
    }}
  };
</script>

<style lang="scss" scoped>
  #submit{
    position: absolute;
    top: 200px;
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
