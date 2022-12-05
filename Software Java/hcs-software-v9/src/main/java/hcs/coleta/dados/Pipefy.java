package hcs.coleta.dados;

import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;

public class Pipefy {

    public void criarCards(String assunto, String descricao) {
        try {
            OkHttpClient client = new OkHttpClient();
            MediaType mediaType = MediaType.parse("application/json");
            RequestBody body = RequestBody.create(mediaType, String.format("{\"query\":\"mutation{   createCard(input:{     pipe_id:302751447,    fields_attributes:[     {field_id:\\\"assunto\\\",       field_value:\\\"%s\\\"},     {field_id:\\\"texto_longo\\\",field_value:\\\"%s\\\"}   ] }) {     card {      id title     }   }   }\"}", assunto, descricao));

            Request request = new Request.Builder()
                    .url("https://api.pipefy.com/graphql")
                    .post(body)
                    .addHeader("accept", "application/json")
                    .addHeader("Authorization", "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDIwODg1NjcsImVtYWlsIjoibWF0aGV1cy5zaWx2YUBzcHRlY2guc2Nob29sIiwiYXBwbGljYXRpb24iOjMwMDIxMzMwOX19.iZPooHUDHJBA1-dXDlzzEYVtmzKAPCIHK0YuY0-IwePMeQobX04Y_g_TM_2nrcR1m7f0oTof9Ey2irE6E1jnnA")
                    .addHeader("Content-Type", "application/json")
                    .build();

            Response response = client.newCall(request).execute();
            System.out.println(response);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
