name := "wikipedia-topic-modeling"

version := "1.0"

scalaVersion := "2.11.7"

resolvers += Resolver.sonatypeRepo("public")

libraryDependencies += "org.apache.spark" %% "spark-core" % "1.6.1"
libraryDependencies += "org.apache.spark" %% "spark-mllib" % "1.6.1"
libraryDependencies += "com.github.scopt" %% "scopt" % "3.4.0"