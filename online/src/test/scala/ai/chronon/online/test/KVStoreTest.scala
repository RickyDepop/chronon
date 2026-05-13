package ai.chronon.online.test

import ai.chronon.api.Constants
import ai.chronon.online.KVStore
import org.scalatest.flatspec.AnyFlatSpec

import scala.util.Success

class KVStoreTest extends AnyFlatSpec {

  it should "include the key and dataset when no latest value exists" in {
    val request =
      KVStore.GetRequest("pricing.price_prediction.v1__1".getBytes(Constants.UTF8), "CHRONON_METADATA")
    val response = KVStore.GetResponse(request, Success(Seq.empty))

    val exception = response.latest.failed.get

    assert(exception.getMessage == "No values found for key 'pricing.price_prediction.v1__1' in dataset CHRONON_METADATA")
  }
}
