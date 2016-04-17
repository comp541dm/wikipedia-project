import org.apache.spark.{SparkContext, SparkConf}

object Main extends App {
  val conf = new SparkConf().setAppName("Simple Application").setMaster("local[2]")
  val sc = new SparkContext(conf)
  val data = sc.textFile("data/split_data/*")

  println("Count: %d".format(data.count()))
  sc.stop()
}
