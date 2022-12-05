package hcs.coleta.dados;

import com.google.protobuf.Message;
import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.text.MessageFormat;

public class Pipefy {

    public static void criarCards(String assunto, String descricao) throws IOException, InterruptedException {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://api.pipefy.com/graphql"))
                .header("accept", "application/json")
                .header("Authorization", "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDIwODg1NjcsImVtYWlsIjoibWF0aGV1cy5zaWx2YUBzcHRlY2guc2Nob29sIiwiYXBwbGljYXRpb24iOjMwMDIxMzMwOX19.iZPooHUDHJBA1-dXDlzzEYVtmzKAPCIHK0YuY0-IwePMeQobX04Y_g_TM_2nrcR1m7f0oTof9Ey2irE6E1jnnA")
                .header("Content-Type", "application/json")
                .method("POST", HttpRequest.BodyPublishers.ofString("{\"query\":\"mutation{ createCard( input:    { pipe_id: \\\"302751447\\\" fields_attributes: "
                            + "[          {field_id: \\\"assunto\\\", field_value: \\\" "+ assunto +" \\\"}          "

                            + "{field_id: \\\"texto_longo\\\", field_value: \\\" "+ descricao +" \\\"} ] } )            "
                        
                            + "{clientMutationId card {id title }}}\"}" ))
                .build();
        HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
        // System.out.println(response.body());
    }

    public static void main(String[] args) throws IOException, InterruptedException {
        criarCards("Teste RAM ", " A memoria ram está atingindo um total de 990%");
    }
}
